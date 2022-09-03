import { fn, sendToProxy } from "./factory";

interface User {
  id: string;
  email: string;
  password: string;
  fullName: string;
  createdAt: string;
  isActive: boolean;
}

type ReducedUser = Omit<User, 'password'>

const usersGet = fn<void, ReducedUser[]>(
  async (args, snekApi) => {
    console.log("args", args);

    return sendToProxy("usersGet", args);
  },
  {
    name: "usersGet",
    decorators: [],
  }
);

export default usersGet;
