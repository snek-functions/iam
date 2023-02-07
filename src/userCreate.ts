import {fn, sendToProxy} from './factory'
import {IUser} from './interfaces'

const userCreate = fn<
  {
    email: string
    password: string
    userId?: string
  },
  IUser
>(
  async (args, snekApi) => {
    console.log('args', args)

    const res: IUser = await sendToProxy('userCreate', args)

    if (res?.userId == undefined) {
      throw new Error('UNIQUE constraint failed')
    }

    return res
  },
  {
    name: 'userCreate',
    decorators: []
  }
)

export default userCreate
