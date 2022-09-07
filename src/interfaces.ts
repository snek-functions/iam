export interface IUser {
  userId: string
  email: string
  password: string
  fullName: string
  createdAt: string
  isActive: boolean
}

export interface IUserDataToken {
  username: string
  firstname: string
  lastname: string
  email: string
}

export interface IReducedUser extends Omit<IUser, 'password'> {}
