import { Router } from "express";
import { notImplemented } from "../controllers/users.controller.js";

const router = Router();
router.all("*", notImplemented);

export default router;