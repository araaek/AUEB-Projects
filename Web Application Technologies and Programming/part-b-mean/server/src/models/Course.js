
import mongoose from "mongoose";

const courseSchema = new mongoose.Schema(
  {
    // Το "id" από το Part A (π.χ. "java", "python-intro") -> το κρατάμε ως slug.
    // Είναι χρήσιμο για URLs τύπου /courses/java
    slug: { type: String, required: true, unique: true, index: true, trim: true },

    title: { type: String, required: true, trim: true },

    category: { type: String, required: true, trim: true },
    categoryLabel: { type: String, default: "", trim: true },

    level: { type: String, default: "", trim: true },
    levelLabel: { type: String, default: "", trim: true },

    image: { type: String, default: "", trim: true },

    shortDescription: { type: String, default: "", trim: true },
    description: { type: String, default: "", trim: true },

    books: { type: [mongoose.Schema.Types.Mixed], default: [] },
    videos: { type: [mongoose.Schema.Types.Mixed], default: [] },
  },
  { timestamps: true }
);

export const Course = mongoose.model("Course", courseSchema);
