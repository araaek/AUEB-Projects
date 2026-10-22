
import mongoose from "mongoose";
import { Course } from "../models/Course.js";

/**
 * Π.χ  GET /api/courses?category=programming&level=advanced&q=java
 */
export async function getCourses(req, res, next) {
  try {
    const { category, level, q } = req.query;

    const filter = {};
    if (category) filter.category = String(category).trim();
    if (level) filter.level = String(level).trim();

    if (q && String(q).trim().length > 0) {
      const safe = String(q).trim();
      filter.$or = [
        { title: { $regex: safe, $options: "i" } },
        { shortDescription: { $regex: safe, $options: "i" } },
        { description: { $regex: safe, $options: "i" } },
      ];
    }


    const courses = await Course.find(filter).sort({ title: 1 }).lean();
    res.json(courses);
  } catch (err) {
    next(err);
  }
}

/**
 * GET /api/courses/:slugOrId
 * Δέχεται είτε Mongo ObjectId είτε το slug (π.χ. "java", "python-intro")
 */
export async function getCourseBySlugOrId(req, res, next) {
  try {
    const { slugOrId } = req.params;

    let course = null;


    if (mongoose.isValidObjectId(slugOrId)) {
      course = await Course.findById(slugOrId).lean();
    }


    if (!course) {
      course = await Course.findOne({ slug: slugOrId }).lean();
    }

    if (!course) {
      return res.status(404).json({ error: "Course not found" });
    }

    res.json(course);
  } catch (err) {
    next(err);
  }
}
