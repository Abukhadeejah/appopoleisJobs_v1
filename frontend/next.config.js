/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: false,
  env: {
    API_URL: 'http://localhost:8000',
    // API_URL: 'https://appopoleisjobs-django-ea3570fedad0.herokuapp.com',
    MAPBOX_ACCESS_TOKEN: 'pk.eyJ1IjoiYXBwb3BvbGkiLCJhIjoiY2xpY2w5ZjF0MDQyazNqbXFteHh4MHJpaSJ9.1g1OVSwRwRl_TJ5mXxOqDQ'
  }
};

module.exports = nextConfig;
