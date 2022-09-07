import {fn, sendToProxy} from './factory'
import {IUserDataToken} from './interfaces'

const userGet = fn<void, IUserDataToken>(
  async (args, snekApi) => {
    console.log('args', args)
    const res: IUserDataToken = await sendToProxy('userGet', args)
    return res
  },
  {
    name: 'userGet',
    decorators: []
  }
)

export default userGet
