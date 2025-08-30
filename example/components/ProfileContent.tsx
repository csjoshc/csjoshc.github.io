import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { Button } from './ui/button';
import { ExternalLink, Mail, MapPin, Calendar, GraduationCap, Briefcase, Code, BookOpen } from 'lucide-react';

export default function ProfileContent() {
  return (
    <div className="container mx-auto px-4 py-8 space-y-12">
      {/* Hero Section */}
      <div className="text-center space-y-6">
        <div className="space-y-4">
          <h1 className="font-bold">Josh Chin</h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Computer Scientist | Researcher | Educator
          </p>
          <p className="text-lg text-muted-foreground max-w-4xl mx-auto">
            Passionate about advancing computational methods, machine learning applications, 
            and creating educational experiences that inspire the next generation of computer scientists.
          </p>
        </div>
        
        <div className="flex flex-wrap items-center justify-center gap-4 text-sm text-muted-foreground">
          <div className="flex items-center gap-2">
            <MapPin className="w-4 h-4" />
            <span>Academic Institution</span>
          </div>
          <div className="flex items-center gap-2">
            <Mail className="w-4 h-4" />
            <span>Research & Collaboration</span>
          </div>
          <div className="flex items-center gap-2">
            <GraduationCap className="w-4 h-4" />
            <span>PhD Computer Science</span>
          </div>
        </div>
      </div>

      {/* About Section */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Briefcase className="w-5 h-5" />
            About
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p>
            I am a computer science researcher and educator with a focus on computational methods, 
            algorithm design, and their practical applications. My work spans theoretical computer science, 
            machine learning applications, and educational technology.
          </p>
          <p>
            Currently pursuing advanced research in computational complexity and algorithm optimization, 
            with a particular interest in bridging the gap between theoretical foundations and real-world applications.
          </p>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 pt-4">
            <div className="text-center">
              <div className="text-2xl font-bold text-primary">5+</div>
              <div className="text-sm text-muted-foreground">Years Research</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-primary">15+</div>
              <div className="text-sm text-muted-foreground">Publications</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-primary">3</div>
              <div className="text-sm text-muted-foreground">Active Projects</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-primary">500+</div>
              <div className="text-sm text-muted-foreground">Students Taught</div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Research Areas */}
      <div className="space-y-6">
        <h2 className="flex items-center gap-2">
          <Code className="w-6 h-6" />
          Research Areas
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>Computational Complexity</CardTitle>
              <CardDescription>
                Theoretical analysis of algorithmic efficiency
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground mb-4">
                Investigating the fundamental limits of computation and developing 
                more efficient algorithms for complex problem domains.
              </p>
              <div className="flex flex-wrap gap-2">
                <Badge variant="secondary">Algorithm Design</Badge>
                <Badge variant="secondary">Complexity Theory</Badge>
                <Badge variant="secondary">Optimization</Badge>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Machine Learning Applications</CardTitle>
              <CardDescription>
                Practical ML solutions for real-world problems
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground mb-4">
                Developing and applying machine learning techniques to solve 
                challenging problems in various domains.
              </p>
              <div className="flex flex-wrap gap-2">
                <Badge variant="secondary">Deep Learning</Badge>
                <Badge variant="secondary">Data Mining</Badge>
                <Badge variant="secondary">Pattern Recognition</Badge>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Educational Technology</CardTitle>
              <CardDescription>
                Innovative approaches to CS education
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground mb-4">
                Creating tools and methodologies to enhance computer science 
                education and make it more accessible.
              </p>
              <div className="flex flex-wrap gap-2">
                <Badge variant="secondary">Interactive Learning</Badge>
                <Badge variant="secondary">Assessment Tools</Badge>
                <Badge variant="secondary">Curriculum Design</Badge>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* Recent Publications */}
      <div className="space-y-6">
        <h2 className="flex items-center gap-2">
          <BookOpen className="w-6 h-6" />
          Recent Publications
        </h2>
        <div className="space-y-4">
          {[
            {
              title: "Efficient Algorithms for Large-Scale Optimization Problems",
              authors: "J. Chin, A. Researcher, B. Collaborator",
              venue: "International Conference on Computational Methods",
              year: "2024",
              type: "Conference Paper"
            },
            {
              title: "Machine Learning Approaches to Educational Assessment",
              authors: "J. Chin, C. Educator",
              venue: "Journal of Educational Technology",
              year: "2023",
              type: "Journal Article"
            },
            {
              title: "Complexity Analysis of Distributed Computing Systems",
              authors: "J. Chin, D. Systems, E. Theorist",
              venue: "Theoretical Computer Science Quarterly",
              year: "2023",
              type: "Journal Article"
            }
          ].map((publication, index) => (
            <Card key={index}>
              <CardContent className="pt-6">
                <div className="space-y-2">
                  <div className="flex items-start justify-between gap-4">
                    <h4 className="font-medium leading-tight">{publication.title}</h4>
                    <Button variant="ghost" size="sm">
                      <ExternalLink className="w-4 h-4" />
                    </Button>
                  </div>
                  <p className="text-sm text-muted-foreground">{publication.authors}</p>
                  <div className="flex items-center gap-4 text-sm text-muted-foreground">
                    <span>{publication.venue}</span>
                    <div className="flex items-center gap-1">
                      <Calendar className="w-3 h-3" />
                      <span>{publication.year}</span>
                    </div>
                    <Badge variant="outline" className="text-xs">
                      {publication.type}
                    </Badge>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      {/* Current Projects */}
      <div className="space-y-6">
        <h2>Current Projects</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>Algorithmic Optimization Framework</CardTitle>
              <CardDescription>
                Open-source library for algorithm benchmarking
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <p className="text-sm text-muted-foreground">
                Developing a comprehensive framework for testing and comparing 
                algorithm performance across different problem domains.
              </p>
              <div className="flex items-center justify-between">
                <div className="flex flex-wrap gap-2">
                  <Badge>Python</Badge>
                  <Badge>C++</Badge>
                  <Badge>Research</Badge>
                </div>
                <Button variant="outline" size="sm">
                  <ExternalLink className="w-4 h-4 mr-1" />
                  View
                </Button>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Educational ML Platform</CardTitle>
              <CardDescription>
                Interactive learning environment for ML concepts
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <p className="text-sm text-muted-foreground">
                Building an interactive platform that helps students understand 
                machine learning concepts through hands-on experimentation.
              </p>
              <div className="flex items-center justify-between">
                <div className="flex flex-wrap gap-2">
                  <Badge>React</Badge>
                  <Badge>Python</Badge>
                  <Badge>Education</Badge>
                </div>
                <Button variant="outline" size="sm">
                  <ExternalLink className="w-4 h-4 mr-1" />
                  View
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* Contact CTA */}
      <Card>
        <CardContent className="pt-6">
          <div className="text-center space-y-4">
            <h3>Interested in Collaboration?</h3>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              I'm always open to discussing research opportunities, academic collaborations, 
              or educational initiatives. Feel free to reach out!
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Button>
                <Mail className="w-4 h-4 mr-2" />
                Contact Me
              </Button>
              <Button variant="outline">
                View CV
                <ExternalLink className="w-4 h-4 ml-2" />
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}