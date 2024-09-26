// types/index.ts

// ユーザー関連の型定義
export interface User {
  id: string;
  username: string;
  email: string;
  createdAt: Date;
  lastLogin: Date;
}

// お茶碗の盛り型の型定義
export enum BowlType {
  VerySmall = 1,
  Small = 2,
  Medium = 3,
  Large = 4,
  VeryLarge = 5,
}

// お茶碗選択の型定義
export interface BowlSelection {
  id: string;
  userId: string;
  bowlType: BowlType;
  createdAt: Date;
}

// 統計データの型定義
export interface Statistics {
  bowlType: BowlType;
  count: number;
  updatedAt: Date;
}

// フィードバックの型定義
export interface Feedback {