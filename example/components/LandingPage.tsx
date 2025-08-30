import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { ChevronRight, Code, Server, BookOpen } from 'lucide-react';

export default function LandingPage() {
  return (
    <div>
      {/* Hero Banner */}
      <div className="bg-gradient-to-br from-background to-muted/30 py-16 px-4">
        <div className="container mx-auto max-w-4xl text-center space-y-6">
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-foreground">
            Welcome to Josh C's Portfolio
          </h1>
          <p className="text-lg md:text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
            A comprehensive learning platform featuring Python, DevOps, and general programming resources 
            with interactive content and hands-on examples.
          </p>
        </div>
      </div>

      {/* Feature Blocks */}
      <div className="container mx-auto max-w-6xl px-4 py-16">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 md:items-stretch">
          
          {/* Python Block */}
          <Card className="group hover:shadow-lg transition-all duration-300 border-border/50 hover:border-border flex flex-col">
            <CardHeader className="space-y-4">
              <div className="w-12 h-12 rounded-lg bg-blue-500/10 dark:bg-blue-400/10 flex items-center justify-center">
                <Code className="w-6 h-6 text-blue-600 dark:text-blue-400" />
              </div>
              <CardTitle className="text-2xl">Python</CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col flex-grow">
              <CardDescription className="text-base leading-relaxed flex-grow">
                Comprehensive Python learning materials covering data science, machine learning, 
                and programming fundamentals with interactive Jupyter notebooks.
              </CardDescription>
              <div className="mt-6 flex justify-center">
                <Button 
                  className="w-full group-hover:bg-primary/90 transition-colors" 
                  size="lg"
                >
                  Explore Python
                  <ChevronRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" />
                </Button>
              </div>
            </CardContent>
          </Card>

          {/* DevOps Block */}
          <Card className="group hover:shadow-lg transition-all duration-300 border-border/50 hover:border-border flex flex-col">
            <CardHeader className="space-y-4">
              <div className="w-12 h-12 rounded-lg bg-green-500/10 dark:bg-green-400/10 flex items-center justify-center">
                <Server className="w-6 h-6 text-green-600 dark:text-green-400" />
              </div>
              <CardTitle className="text-2xl">DevOps</CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col flex-grow">
              <CardDescription className="text-base leading-relaxed flex-grow">
                Learn through hands-on examples and interactive content. All materials are 
                organized and easy to navigate for self-paced learning.
              </CardDescription>
              <div className="mt-6 flex justify-center">
                <Button 
                  className="w-full group-hover:bg-primary/90 transition-colors" 
                  size="lg"
                >
                  Explore DevOps
                  <ChevronRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" />
                </Button>
              </div>
            </CardContent>
          </Card>

          {/* General Block */}
          <Card className="group hover:shadow-lg transition-all duration-300 border-border/50 hover:border-border flex flex-col">
            <CardHeader className="space-y-4">
              <div className="w-12 h-12 rounded-lg bg-purple-500/10 dark:bg-purple-400/10 flex items-center justify-center">
                <BookOpen className="w-6 h-6 text-purple-600 dark:text-purple-400" />
              </div>
              <CardTitle className="text-2xl">General</CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col flex-grow">
              <CardDescription className="text-base leading-relaxed flex-grow">
                Latest update: August 28, 2025. View the most recent site updates and changes.
              </CardDescription>
              <div className="mt-6 flex justify-center">
                <Button 
                  className="w-full group-hover:bg-primary/90 transition-colors" 
                  size="lg"
                >
                  Explore General
                  <ChevronRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" />
                </Button>
              </div>
            </CardContent>
          </Card>

        </div>
      </div>
    </div>
  );
}