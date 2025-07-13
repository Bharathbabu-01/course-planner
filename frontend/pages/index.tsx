import { useEffect, useState } from 'react';

type Course = { id: number; code: string; title: string; credits: number };

export default function Home() {
  const [courses, setCourses] = useState<Course[]>([]);

  useEffect(() => {
    fetch('http://localhost:8000/courses')
      .then((r) => r.json())
      .then(setCourses);
  }, []);

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">ASU Course Planner</h1>
      <ul>
        {courses.map((c) => (
          <li key={c.id}>{c.code} – {c.title} ({c.credits} cr)</li>
        ))}
      </ul>
    </main>
  );
}
