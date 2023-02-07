import {fn, sendToProxy} from './factory'

const aliasCheck = fn<
  {
    alias: string
  },
  boolean
>(
  async (args, snekApi) => {
    console.log('args', args)

    return sendToProxy('aliasCheck', args)
  },
  {
    name: 'aliasCheck',
    decorators: []
  }
)

export default aliasCheck
