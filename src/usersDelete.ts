import { fn, sendToProxy } from "./factory";

const usersDelete = fn<
  {
    user_id: string
  },
  boolean
>(
  async (args, snekApi) => {
    console.log("args", args);

    return sendToProxy("usersDelete", args);
  },
  {
    name: "usersDelete",
    decorators: [],
  }
);

export default usersDelete;
