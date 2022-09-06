import {fn, sendToProxy} from './factory'
import {IUser} from './interfaces'

const usersUpdate = fn<
  {
    userId: string
    email: string
    password?: string
    firstName?: string
    lastName?: string
    isActive?: boolean
  },
  IUser
>(
  async (args, snekApi) => {
    console.log('args', args)
    const res: IUser = await sendToProxy('usersUpdate', args)

    if (res?.userId == undefined) {
      throw new Error('Oh no! Something has gone wrong.')
    }

    await sendToProxy('publishAuth', args)

    return res
  },
  {
    name: 'usersUpdate',
    decorators: []
  }
)

export default usersUpdate
