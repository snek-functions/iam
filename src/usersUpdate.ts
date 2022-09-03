import { fn, sendToProxy } from "./factory";

interface User {
  id: string;
  email: string;
  password: string;
  fullName: string;
  createdAt: string;
  isActive: boolean;
}

const usersUpdate = fn<
  {
    email: string;
    password: string;
    firstName?: string
    lastName?: string
    isActive?: boolean
  },
  User
>(
  async (args, snekApi) => {
    console.log("args", args);

    return sendToProxy("usersUpdate", args);
  },
  {
    name: "usersUpdate",
    decorators: [],
  }
);

export default usersUpdate;
