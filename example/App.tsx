import ResponsiveNav from './components/ResponsiveNav';
import LandingPage from './components/LandingPage';
import { ThemeProvider } from './components/ThemeProvider';

export default function App() {
  return (
    <ThemeProvider defaultTheme="system" storageKey="csjoshc-theme">
      <div className="min-h-screen bg-background">
        <ResponsiveNav />
        <LandingPage />
      </div>
    </ThemeProvider>
  );
}