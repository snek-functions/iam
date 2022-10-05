import {fn, sendToProxy} from './factory'
import {IReducedUser} from './interfaces'

const usersGet = fn<{}, IReducedUser[]>(
  async (args, snekApi) => {
    console.log('args', args)
    const res: IReducedUser[] = await sendToProxy('usersGet', args)

    if (!Array.isArray(res)) {
      throw new Error('Oh no! Something has gone wrong.')
    }

    return res
  },
  {
    name: 'usersGet',
    decorators: []
  }
)

export default usersGet
