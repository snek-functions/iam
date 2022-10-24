import { fn, sendToProxy } from './factory'
import { IReducedUser } from './interfaces'

export interface UserGetByUserIdArgs {
  userId: string
}

export interface UserGetByAliasArgs {
  alias: string
}

export type UserGetArgs = UserGetByUserIdArgs | UserGetByAliasArgs

const userGet = fn<UserGetArgs, IReducedUser>(
  async (args, snekApi) => {
    console.log('args', args)
    const res: IReducedUser = await sendToProxy('userGet', args)

    if (!res.userId || res.userId === '0')
      throw new Error(
        `Unable to find: ${
          (args as UserGetByAliasArgs).alias ||
          (args as UserGetByUserIdArgs).userId
        }`
      )

    return res
  },
  {
    name: 'userGet',
    decorators: []
  }
)

export default userGet
