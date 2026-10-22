import mongoose from "mongoose";

const reviewSchema = new mongoose.Schema(
  {
    // Stub: π.χ. userId, courseId, rating, comment
  },
  { timestamps: true }
);

export const Review = mongoose.model("Review", reviewSchema);
