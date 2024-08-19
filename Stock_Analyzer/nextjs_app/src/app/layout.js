import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Stock Guru AI | Your Ultimate Companion for Stock Investment & Analysis",
  description: "Discover powerful insights and tools for effective stock investment and analysis, all in one place with Stock Guru AI.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {children}
        <footer style={{ position: "fixed", bottom: 0, width: "100%", padding: "10px", textAlign: "center", backgroundColor: "#f1f1f1" }}>
          <p>&copy; 2024 Stock Guru AI. All rights reserved.</p>
        </footer>
      </body>
    </html>
  );
}