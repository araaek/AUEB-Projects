import Enrollment from '../models/Enrollment.js';

export async function createEnrollment(req, res) {
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
}
