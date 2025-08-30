import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { Button } from './ui/button';
import { ExternalLink, Mail, MapPin, Calendar, GraduationCap, Briefcase, Code, BookOpen, Github } from 'lucide-react';
import { personalInfo, researchAreas, publications, projects, socialLinks } from '../data/portfolio-data';

export default function RealProfileContent() {
  return (
    <div className="container mx-auto px-4 py-8 space-y-12">
      {/* Hero Section */}
      <div className="text-center space-y-6">
        <div className="space-y-4">
          {personalInfo.profileImage && (
            <div className="w-32 h-32 mx-auto rounded-full overflow-hidden bg-muted">
              <img 
                src={personalInfo.profileImage} 
                alt={personalInfo.name}
                className="w-full h-full object-cover"
              />
            </div>
          )}
          <h1 className="font-bold">{personalInfo.name}</h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            {personalInfo.title}
          </p>
          <p className="text-lg text-muted-foreground max-w-4xl mx-auto">
            {personalInfo.bio}
          </p>
        </div>
        
        <div className="flex flex-wrap items-center justify-center gap-4 text-sm text-muted-foreground">
          <div className="flex items-center gap-2">
            <MapPin className="w-4 h-4" />
            <span>{personalInfo.location}</span>
          </div>
          <div className="flex items-center gap-2">
            <GraduationCap className="w-4 h-4" />
            <span>{personalInfo.institution}</span>
          </div>
          <div className="flex items-center gap-2">
            <Mail className="w-4 h-4" />
            <span>{personalInfo.email}</span>
          </div>
        </div>
      </div>

      {/* Quick Stats */}
      <Card>
        <CardContent className="pt-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="text-center">
              <div className="text-2xl font-bold text-primary">{researchAreas.length}</div>
              <div className="text-sm text-muted-foreground">Research Areas</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-primary">{publications.length}</div>
              <div className="text-sm text-muted-foreground">Publications</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-primary">{projects.length}</div>
              <div className="text-sm text-muted-foreground">Projects</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-primary">{projects.filter(p => p.status === 'Active').length}</div>
              <div className="text-sm text-muted-foreground">Active Projects</div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Research Areas */}
      {researchAreas.length > 0 && (
        <div className="space-y-6">
          <h2 className="flex items-center gap-2">
            <Code className="w-6 h-6" />
            Research Areas
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {researchAreas.map((area, index) => (
              <Card key={index}>
                <CardHeader>
                  <CardTitle>{area.title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-muted-foreground mb-4">
                    {area.description}
                  </p>
                  <div className="flex flex-wrap gap-2">
                    {area.keywords.map((keyword, kidx) => (
                      <Badge key={kidx} variant="secondary">{keyword}</Badge>
                    ))}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}

      {/* Publications */}
      {publications.length > 0 && (
        <div className="space-y-6">
          <h2 className="flex items-center gap-2">
            <BookOpen className="w-6 h-6" />
            Publications
          </h2>
          <div className="space-y-4">
            {publications.map((publication, index) => (
              <Card key={index}>
                <CardContent className="pt-6">
                  <div className="space-y-2">
                    <div className="flex items-start justify-between gap-4">
                      <h4 className="font-medium leading-tight">{publication.title}</h4>
                      {publication.url && (
                        <Button 
                          variant="ghost" 
                          size="sm"
                          onClick={() => window.open(publication.url, '_blank')}
                        >
                          <ExternalLink className="w-4 h-4" />
                        </Button>
                      )}
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
      )}

      {/* Projects */}
      {projects.length > 0 && (
        <div className="space-y-6">
          <h2>Projects</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {projects.map((project, index) => (
              <Card key={index}>
                <CardHeader>
                  <CardTitle className="flex items-center justify-between">
                    {project.title}
                    <Badge variant={project.status === 'Active' ? 'default' : 'secondary'}>
                      {project.status}
                    </Badge>
                  </CardTitle>
                  <CardDescription>
                    {project.description}
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="flex flex-wrap gap-2">
                    {project.technologies.map((tech, tidx) => (
                      <Badge key={tidx} variant="outline">{tech}</Badge>
                    ))}
                  </div>
                  <div className="flex items-center gap-2">
                    {project.url && (
                      <Button 
                        variant="outline" 
                        size="sm"
                        onClick={() => window.open(project.url, '_blank')}
                      >
                        <ExternalLink className="w-4 h-4 mr-1" />
                        View Live
                      </Button>
                    )}
                    {project.githubUrl && (
                      <Button 
                        variant="outline" 
                        size="sm"
                        onClick={() => window.open(project.githubUrl, '_blank')}
                      >
                        <Github className="w-4 h-4 mr-1" />
                        Code
                      </Button>
                    )}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}

      {/* Contact CTA */}
      <Card>
        <CardContent className="pt-6">
          <div className="text-center space-y-4">
            <h3>Get In Touch</h3>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Interested in collaboration, research opportunities, or have questions about my work? 
              I'd love to hear from you!
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Button onClick={() => window.open(`mailto:${personalInfo.email}`, '_blank')}>
                <Mail className="w-4 h-4 mr-2" />
                Email Me
              </Button>
              {personalInfo.cv && (
                <Button variant="outline" onClick={() => window.open(personalInfo.cv, '_blank')}>
                  View CV
                  <ExternalLink className="w-4 h-4 ml-2" />
                </Button>
              )}
              {socialLinks.github && (
                <Button variant="outline" onClick={() => window.open(socialLinks.github, '_blank')}>
                  <Github className="w-4 h-4 mr-2" />
                  GitHub
                </Button>
              )}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Instructions for updating content */}
      <Card className="border-dashed border-2 border-muted-foreground/20">
        <CardContent className="pt-6">
          <div className="text-center space-y-4">
            <h3 className="text-muted-foreground">🔄 Replace with Your Content</h3>
            <p className="text-sm text-muted-foreground max-w-2xl mx-auto">
              To use your actual GitHub content:
            </p>
            <div className="text-left max-w-xl mx-auto space-y-2 text-sm text-muted-foreground">
              <p>1. Copy your content from <code className="bg-muted px-1 py-0.5 rounded">https://github.com/csjoshc/csjoshc.github.io</code></p>
              <p>2. Update the data in <code className="bg-muted px-1 py-0.5 rounded">/data/portfolio-data.ts</code></p>
              <p>3. Replace the placeholder content with your actual information</p>
              <p>4. Add your images to the project and update the image paths</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}