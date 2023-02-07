import {fn, sendToProxy} from './factory'

const authenticationPublish = fn(
  async args => {
    return sendToProxy('authenticationPublish', args)
  },
  {
    name: 'authenticationPublish',
    decorators: []
  }
)

export default authenticationPublish
