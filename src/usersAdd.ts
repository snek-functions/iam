import { fn, sendToProxy } from "./factory";

interface User {
  id: string;
  email: string;
  password: string;
  fullName: string;
  createdAt: string;
  isActive: boolean;
}

const usersAdd = fn<
  {
    email: string;
    password: string;
  },
  User
>(
  async (args, snekApi) => {
    console.log("args", args);

    return sendToProxy("usersAdd", args);
  },
  {
    name: "usersAdd",
    decorators: [],
  }
);

export default usersAdd;
