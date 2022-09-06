import {fn, sendToProxy} from './factory'

const aliasAvailable = fn<
  {
    alias: string
  },
  boolean
>(
  async (args, snekApi) => {
    console.log('args', args)

    return sendToProxy('aliasAvailable', args)
  },
  {
    name: 'aliasAvailable',
    decorators: []
  }
)

export default aliasAvailable
