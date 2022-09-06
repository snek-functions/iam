import {fn, sendToProxy} from './factory'
import {IUser} from './interfaces'

const usersAdd = fn<
  {
    email: string
    password: string
  },
  IUser
>(
  async (args, snekApi) => {
    console.log('args', args)

    const res: IUser = await sendToProxy('usersAdd', args)

    if (res?.userId == undefined) {
      throw new Error('UNIQUE constraint failed')
    }

    return res
  },
  {
    name: 'usersAdd',
    decorators: []
  }
)

export default usersAdd
