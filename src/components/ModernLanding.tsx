import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { ChevronRight, Code, Server, BookOpen, Github, Linkedin } from 'lucide-react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function ModernLanding() {
  const { siteConfig } = useDocusaurusContext();

  const featureCards = [
    {
      title: 'Python',
      description: 'Comprehensive Python learning materials covering data science, machine learning, and programming fundamentals with interactive Jupyter notebooks.',
      icon: <Code className="w-6 h-6 text-blue-600 dark:text-blue-400" />,
      iconBg: 'bg-blue-500/10 dark:bg-blue-400/10',
      link: '/docs/Python/base',
      color: 'text-blue-600 dark:text-blue-400',
    },
    {
      title: 'DevOps',
      description: 'Learn through hands-on examples and interactive content. All materials are organized and easy to navigate for self-paced learning.',
      icon: <Server className="w-6 h-6 text-green-600 dark:text-green-400" />,
      iconBg: 'bg-green-500/10 dark:bg-green-400/10',
      link: '/docs/Devops/roadmap_notes',
      color: 'text-green-600 dark:text-green-400',
    },
    {
      title: 'General',
      description: 'Latest update: August 28, 2025. Major Site Overhaul - August 2025',
      icon: <BookOpen className="w-6 h-6 text-purple-600 dark:text-purple-400" />,
      iconBg: 'bg-purple-500/10 dark:bg-purple-400/10',
      link: '/blog/major-site-overhaul-2025',
      color: 'text-purple-600 dark:text-purple-400',
    },
  ];

  const quickLinks = [
    {
      title: 'Linux Fundamentals',
      description: 'Essential Linux command line and system administration',
      link: '/docs/Linux/base',
      icon: <Server className="w-5 h-5" />,
    },
    {
      title: 'GitHub Workflow',
      description: 'Version control and collaboration best practices',
      link: '/docs/Github/intro_gh',
      icon: <Github className="w-5 h-5" />,
    },
  ];

  return (
    <div className="min-h-screen bg-background">
      {/* Hero Banner */}
      <div className="bg-gradient-to-br from-background to-muted/30 py-16 px-4">
        <div className="container mx-auto max-w-4xl text-center space-y-6">
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-foreground">
            Welcome to {siteConfig.title}
          </h1>
          <p className="text-lg md:text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
            {siteConfig.tagline}
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <Button 
              size="lg"
              onClick={() => window.location.href = '/docs/Python/base'}
              className="flex items-center gap-2"
            >
              Start Learning
              <ChevronRight className="w-4 h-4" />
            </Button>
            <Button 
              variant="outline" 
              size="lg"
              onClick={() => window.location.href = '/blog'}
            >
              View Updates
            </Button>
          </div>
        </div>
      </div>

      {/* Feature Blocks */}
      <div className="container mx-auto max-w-6xl px-4 py-16">
        <h2 className="text-3xl font-bold text-center mb-12 text-foreground">
          Learning Paths
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 md:items-stretch">
          {featureCards.map((card) => (
            <Card key={card.title} className="group hover:shadow-lg transition-all duration-300 border-border/50 hover:border-border flex flex-col">
              <CardHeader className="space-y-4">
                <div className={`w-12 h-12 rounded-lg ${card.iconBg} flex items-center justify-center`}>
                  {card.icon}
                </div>
                <CardTitle className="text-2xl">{card.title}</CardTitle>
              </CardHeader>
              <CardContent className="flex flex-col flex-grow">
                <CardDescription className="text-base leading-relaxed flex-grow">
                  {card.description}
                </CardDescription>
                <div className="mt-6 flex justify-center">
                  <Button 
                    className="w-full group-hover:bg-primary/90 transition-colors" 
                    size="lg"
                    onClick={() => window.location.href = card.link}
                  >
                    Explore {card.title}
                    <ChevronRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" />
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      {/* Quick Links Section */}
      <div className="container mx-auto max-w-6xl px-4 py-16">
        <h2 className="text-3xl font-bold text-center mb-12 text-foreground">
          Quick Access
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {quickLinks.map((link) => (
            <Card key={link.title} className="group hover:shadow-lg transition-all duration-300 border-border/50 hover:border-border">
              <CardContent className="p-6">
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 rounded-lg bg-muted flex items-center justify-center">
                    {link.icon}
                  </div>
                  <div className="flex-1">
                    <h3 className="text-xl font-semibold mb-2 text-foreground">{link.title}</h3>
                    <p className="text-muted-foreground mb-4">{link.description}</p>
                    <Button 
                      variant="outline" 
                      onClick={() => window.location.href = link.link}
                      className="group-hover:bg-primary group-hover:text-primary-foreground transition-colors"
                    >
                      Learn More
                      <ChevronRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" />
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      {/* Social Links */}
      <div className="container mx-auto max-w-6xl px-4 py-16">
        <div className="text-center">
          <h2 className="text-2xl font-bold mb-6 text-foreground">Connect & Collaborate</h2>
          <div className="flex justify-center gap-4">
            <Button 
              variant="outline" 
              size="lg"
              onClick={() => window.open('https://github.com/csjoshc', '_blank')}
              className="flex items-center gap-2"
            >
              <Github className="w-5 h-5" />
              GitHub
            </Button>
            <Button 
              variant="outline" 
              size="lg"
              onClick={() => window.open('https://linkedin.com/in/csjoshc', '_blank')}
              className="flex items-center gap-2"
            >
              <Linkedin className="w-5 h-5" />
              LinkedIn
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}
