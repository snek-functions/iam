export interface IUser {
  userId: string
  email: string
  password: string
  firstName: string
  lastName: string
  createdAt: string
  isActive: boolean
}

export interface IReducedUser extends Omit<IUser, 'password'> {}
