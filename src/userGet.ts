import {fn, sendToProxy} from './factory'
import {IReducedUser} from './interfaces'

const userGet = fn<{}, IReducedUser>(
  async (args, snekApi) => {
    console.log('args', args)
    const res: IReducedUser = await sendToProxy('userGet', args)
    return res
  },
  {
    name: 'userGet',
    decorators: []
  }
)

export default userGet
