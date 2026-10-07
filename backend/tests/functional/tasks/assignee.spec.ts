import User from '#models/user'
import { test } from '@japa/runner'
import testUtils from '@adonisjs/core/services/test_utils'

/**
 * Lo que una tarea enseña de su responsable. Cubre el requisito «Lo que cada
 * tarea muestra de su responsable» de `openspec/specs/tasks/spec.md`, por las
 * dos lecturas de tareas: la lista y la tarea suelta.
 */
test.group('Tasks | responsable', (group) => {
  group.each.setup(() => testUtils.db().withGlobalTransaction())

  async function sesion(client: any, fullName: string | null, email = 'ada@example.com') {
    await User.create({ fullName, email, password: 'secreto123' })

    const response = await client.post('/api/v1/auth/login').json({ email, password: 'secreto123' })

    return response.body().data.token as string
  }

  async function crearTarea(client: any, token: string) {
    const response = await client
      .post('/api/v1/tasks')
      .header('Authorization', `Bearer ${token}`)
      .json({ title: 'Revisar el informe' })

    response.assertStatus(201)
    return response.body().data.id as number
  }

  test('el responsable llega con su nombre y sus iniciales', async ({ client, assert }) => {
    const token = await sesion(client, 'Ada Lovelace')
    const id = await crearTarea(client, token)

    const lista = await client.get('/api/v1/tasks').header('Authorization', `Bearer ${token}`)
    lista.assertStatus(200)
    const enLista = lista.body().data.find((tarea: { id: number }) => tarea.id === id)
    assert.equal(enLista.assignee.fullName, 'Ada Lovelace')
    assert.equal(enLista.assignee.initials, 'AL')

    const suelta = await client
      .get(`/api/v1/tasks/${id}`)
      .qs({ today: '2026-10-07' })
      .header('Authorization', `Bearer ${token}`)
    suelta.assertStatus(200)
    assert.equal(suelta.body().data.assignee.fullName, 'Ada Lovelace')
    assert.equal(suelta.body().data.assignee.initials, 'AL')
  })

  test('el responsable no trae el email ni datos de acceso', async ({ client, assert }) => {
    const token = await sesion(client, 'Ada Lovelace')
    const id = await crearTarea(client, token)

    const lista = await client.get('/api/v1/tasks').header('Authorization', `Bearer ${token}`)
    lista.assertStatus(200)
    const enLista = lista.body().data.find((tarea: { id: number }) => tarea.id === id)

    const suelta = await client
      .get(`/api/v1/tasks/${id}`)
      .qs({ today: '2026-10-07' })
      .header('Authorization', `Bearer ${token}`)
    suelta.assertStatus(200)

    // «Datos de acceso» son los que abren la cuenta: el email con el que se
    // entra, la contraseña y el token. Se mira la clave y también el valor, por
    // si alguno saliera con otro nombre.
    for (const assignee of [enLista.assignee, suelta.body().data.assignee]) {
      assert.notProperty(assignee, 'email')
      assert.notProperty(assignee, 'password')

      const serialized = JSON.stringify(assignee)
      assert.notInclude(serialized, 'ada@example.com')
      assert.notInclude(serialized, 'secreto123')
      assert.notInclude(serialized, token)
    }
  })

  test('un responsable sin nombre llega con el nombre nulo y sus iniciales', async ({
    client,
    assert,
  }) => {
    const token = await sesion(client, null)
    const id = await crearTarea(client, token)

    const lista = await client.get('/api/v1/tasks').header('Authorization', `Bearer ${token}`)
    lista.assertStatus(200)
    const enLista = lista.body().data.find((tarea: { id: number }) => tarea.id === id)
    assert.isNull(enLista.assignee.fullName)
    assert.equal(enLista.assignee.initials, 'AE')

    const suelta = await client
      .get(`/api/v1/tasks/${id}`)
      .qs({ today: '2026-10-07' })
      .header('Authorization', `Bearer ${token}`)
    suelta.assertStatus(200)
    assert.isNull(suelta.body().data.assignee.fullName)
    assert.equal(suelta.body().data.assignee.initials, 'AE')
  })
})
