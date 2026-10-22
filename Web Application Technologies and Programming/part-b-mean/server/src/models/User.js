import mongoose from "mongoose";

const userSchema = new mongoose.Schema(
  {
    // Stub: πεδία θα οριστούν σε μελλοντική υλοποίηση
  },
  { timestamps: true }
);

export const User = mongoose.model("User", userSchema);
