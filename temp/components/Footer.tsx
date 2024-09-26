import Link from 'next/link'

const Footer = () => {
  const currentYear = new Date().getFullYear()

  return (
    <footer className="bg-gray-100 border-t border-gray-200">
      <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="mb-4 md:mb-0">
            <p className="text-gray-600 text-sm">
              © {currentYear} NormaBowl. All rights reserved.
            </p>
          </div>
          <div className="flex space-x-6">
            <Link
              href="/privacy-policy"
              className="text-gray-600 hover:text-gray-900 text-sm transition duration-150 ease-in-out"
            >
              プライバシーポリシー
            </Link>
            <Link
              href="/contact"
              className