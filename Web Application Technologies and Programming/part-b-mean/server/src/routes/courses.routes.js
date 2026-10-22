
import { Router } from "express";
import {
  getCourses,
  getCourseBySlugOrId,
} from "../controllers/courses.controller.js";

const router = Router();

router.get("/", getCourses);
router.get("/:slugOrId", getCourseBySlugOrId);

export default router;
