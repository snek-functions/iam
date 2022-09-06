export interface IUser {
  userId: string
  email: string
  password: string
  fullName: string
  createdAt: string
  isActive: boolean
}

export interface IReducedUser extends Omit<IUser, 'password'> {}
