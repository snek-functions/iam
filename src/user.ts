import {fn, sendToProxy} from './factory'
import {IReducedUser} from './interfaces'

export interface UserByUserIdArgs {
  userId: string
}

export interface UserByAliasArgs {
  alias: string
}

export type UserArgs = UserByUserIdArgs | UserByAliasArgs

const user = fn<UserArgs, IReducedUser>(
  async (args, snekApi) => {
    console.log('args', args)
    const res: IReducedUser = await sendToProxy('user', args)

    if (!res.userId || res.userId === '0')
      throw new Error(
        `Unable to find: ${
          (args as UserByAliasArgs).alias || (args as UserByUserIdArgs).userId
        }`
      )

    return res
  },
  {
    name: 'user',
    decorators: []
  }
)

export default user
