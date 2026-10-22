import express from 'express';
import Enrollment from '../models/Enrollment.js';

const router = express.Router();

// POST /api/enrollments  – καταχώριση εγγραφής
router.post('/', async (req, res) => {
  try {
    const enrollment = await Enrollment.create({
      firstName: req.body.firstName,
      lastName: req.body.lastName,
      email: req.body.email,
      password: req.body.password,           
      level: req.body.level,
      categories: req.body.categories || [],
      courses: req.body.courses || []
    });

    res.status(201).json({ message: 'ok', id: enrollment._id });
  } catch (err) {
    console.error('Enrollment save error:', err);
    res.status(500).json({ message: 'Server error' });
  }
});

// GET /api/enrollments  – λίστα όλων των εγγραφών
router.get('/', async (req, res) => {
  try {
    const enrollments = await Enrollment.find().sort({ createdAt: -1 });
    res.json(enrollments);
  } catch (err) {
    console.error('Enrollment list error:', err);
    res.status(500).json({ message: 'Server error' });
  }
});

export default router;
