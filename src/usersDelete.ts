import { fn, sendToProxy } from './factory'

const usersDelete = fn<
  {
    userId: string
  },
  boolean
>(
  async (args, snekApi) => {
    console.log('args', args)

    const res: boolean = await sendToProxy('usersDelete', args)

    if (!res) {
      throw new Error('User could not be deleted.')
    }

    return res
  },
  {
    name: 'usersDelete',
    decorators: []
  }
)

export default usersDelete
