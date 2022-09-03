import { fn, sendToProxy } from "./factory";

const publishAuth = fn(
  async (args) => {
    return sendToProxy("publishAuth", args);
  },
  {
    name: "publishAuth",
    decorators: []
  }
);

export default publishAuth;
