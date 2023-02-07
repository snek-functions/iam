import {fn, sendToProxy} from './factory'
import {IReducedUser} from './interfaces'

const users = fn<{}, IReducedUser[]>(
  async (args, snekApi) => {
    console.log('args', args)
    const res: IReducedUser[] = await sendToProxy('users', args)

    if (!Array.isArray(res)) {
      throw new Error('Oh no! Something has gone wrong.')
    }

    return res
  },
  {
    name: 'users',
    decorators: []
  }
)

export default users
