

import React, { useState } from "react";

export default function NewsApp() {
  const [selectedCategory, setSelectedCategory] = useState("Semua");

  const categories = ["Semua", "Teknologi", "Politik", "Olahraga", "Hiburan"];

  const articles = [
    {
      id: 1,
      title: "Teknologi AI Semakin Berkembang",
      category: "Teknologi",
      content:
        "Perkembangan kecerdasan buatan semakin pesat dan mulai diterapkan di berbagai sektor industri.",
    },
    {
      id: 2,
      title: "Pemilu dan Tantangan Demokrasi",
      category: "Politik",
      content:
        "Pemilu menjadi ujian penting bagi stabilitas demokrasi dan partisipasi masyarakat.",
    },
    {
      id: 3,
      title: "Tim Nasional Raih Kemenangan",
      category: "Olahraga",
      content:
        "Tim nasional berhasil meraih kemenangan penting dalam laga persahabatan.",
    },
    {
      id: 4,
      title: "Film Lokal Tembus Pasar Internasional",
      category: "Hiburan",
      content:
        "Film karya anak bangsa berhasil menarik perhatian penonton internasional.",
    },
  ];

  const filteredArticles =
    selectedCategory === "Semua"
      ? articles
      : articles.filter((a) => a.category === selectedCategory);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <header className="mb-6">
        <h1 className="text-3xl font-bold mb-2">Portal Berita</h1>
        <nav className="flex gap-2">
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-1 rounded ${
                selectedCategory === cat
                  ? "bg-blue-600 text-white"
                  : "bg-white border"
              }`}
            >
              {cat}
            </button>
          ))}
        </nav>
      </header>

      <main className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filteredArticles.map((article) => (
          <article
            key={article.id}
            className="bg-white p-4 rounded shadow"
          >
            <h2 className="text-xl font-semibold mb-1">{article.title}</h2>
            <span className="text-sm text-gray-500">
              {article.category}
            </span>
            <p className="mt-2 text-gray-700">{article.content}</p>
          </article>
        ))}
      </main>
    </div>
  );
}
