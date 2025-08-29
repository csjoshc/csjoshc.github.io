/**
 * Latest Post Navigator - Inline Version
 * This script is embedded directly into HTML during the build process
 * No external JSON files needed - everything is inline
 */

class InlineLatestPostNavigator {
    constructor() {
        this.init();
    }

    /**
     * Initialize the navigator
     */
    init() {
        this.createLatestPostButton();
    }

    /**
     * Create a button to navigate to the latest post
     */
    createLatestPostButton() {
        // Check if button already exists
        if (document.getElementById('latest-post-btn')) {
            return;
        }

        const button = document.createElement('button');
        button.id = 'latest-post-btn';
        button.className = 'latest-post-button';
        button.innerHTML = '📅 Go to Latest Post';
        button.style.cssText = `
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            margin: 20px 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        `;

        // Add hover effects
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'translateY(-2px)';
            button.style.boxShadow = '0 6px 20px rgba(0,0,0,0.3)';
        });

        button.addEventListener('mouseleave', () => {
            button.style.transform = 'translateY(0)';
            button.style.boxShadow = '0 4px 15px rgba(0,0,0,0.2)';
        });

        // Add click handler
        button.addEventListener('click', () => {
            this.navigateToLatestPost();
        });

        // Insert button after the main heading
        const heading = document.querySelector('h1');
        if (heading) {
            heading.parentNode.insertBefore(button, heading.nextSibling);
        } else {
            // Fallback: insert at the beginning of the body
            document.body.insertBefore(button, document.body.firstChild);
        }

        // Update button with latest post info if available
        this.updateButtonWithLatestPost();
    }

    /**
     * Update button with latest post information
     */
    updateButtonWithLatestPost() {
        // Look for the latest post link in the page
        const latestPostLink = this.findLatestPostLink();
        if (latestPostLink) {
            const button = document.getElementById('latest-post-btn');
            if (button) {
                const linkText = latestPostLink.textContent.trim();
                const date = this.extractDateFromLink(linkText);
                button.innerHTML = `📅 Latest: ${date}`;
                button.title = `Click to go to the most recent post from ${date}`;
                
                // Store the latest post URL for navigation
                this.latestPostUrl = latestPostLink.href;
            }
        }
    }

    /**
     * Find the latest post link by scanning the page content
     */
    findLatestPostLink() {
        // Look for links in the first month section (most recent)
        const monthSections = document.querySelectorAll('h2');
        for (const section of monthSections) {
            const sectionText = section.textContent.toLowerCase();
            // Skip non-month sections
            if (!sectionText.includes('2025') && !sectionText.includes('2019')) {
                continue;
            }
            
            // Find the first link in this section (most recent post)
            const nextElement = section.nextElementSibling;
            if (nextElement && nextElement.tagName === 'UL') {
                const firstLink = nextElement.querySelector('li:first-child a');
                if (firstLink) {
                    return firstLink;
                }
            }
        }
        return null;
    }

    /**
     * Extract date from link text
     */
    extractDateFromLink(linkText) {
        // Handle various date formats
        const dateMatch = linkText.match(/(\d{1,2})[\/\-_](\d{1,2})[\/\-_](\d{4})/);
        if (dateMatch) {
            const [_, day, month, year] = dateMatch;
            const monthNames = [
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
            ];
            return `${monthNames[parseInt(month) - 1]} ${day}, ${year}`;
        }
        
        // Handle other date formats
        if (linkText.includes('August 28, 2025')) return 'Aug 28, 2025';
        if (linkText.includes('June 15, 2019')) return 'Jun 15, 2019';
        if (linkText.includes('May 25, 2019')) return 'May 25, 2019';
        
        return 'Latest Post';
    }

    /**
     * Navigate to the latest post
     */
    navigateToLatestPost() {
        if (this.latestPostUrl) {
            window.location.href = this.latestPostUrl;
        } else {
            // Fallback: try to find and navigate to the latest post
            const latestPostLink = this.findLatestPostLink();
            if (latestPostLink) {
                window.location.href = latestPostLink.href;
            } else {
                alert('Could not find the latest post. Please check the site updates manually.');
            }
        }
    }
}

// Auto-initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new InlineLatestPostNavigator();
});

// Also initialize if script is loaded after DOM
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new InlineLatestPostNavigator();
    });
} else {
    new InlineLatestPostNavigator();
}
