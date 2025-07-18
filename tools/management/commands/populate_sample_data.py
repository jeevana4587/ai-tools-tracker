from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tools.models import Category, Tool
from reviews.models import Review
import random

class Command(BaseCommand):
    help = 'Populate database with sample data for analytics charts'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data for analytics...')
        
        # Create categories if they don't exist
        categories_data = [
            {'name': 'Image'},
            {'name': 'Code'},
            {'name': 'Research'},
            {'name': 'Video'},
            {'name': 'Audio'},
            {'name': 'Writing'},
            {'name': 'Productivity'},
            {'name': 'Design'}
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(name=cat_data['name'])
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Sample tools data
        tools_data = [
            # Image tools
            {'name': 'Midjourney', 'category': 'Image', 'website': 'https://midjourney.com', 'description': 'AI art generation tool', 'access_type': 'Paid'},
            {'name': 'DALL-E 3', 'category': 'Image', 'website': 'https://openai.com/dall-e-3', 'description': 'OpenAI image generation', 'access_type': 'Paid'},
            {'name': 'Stable Diffusion', 'category': 'Image', 'website': 'https://stability.ai', 'description': 'Open source image generation', 'access_type': 'Free'},
            {'name': 'Canva AI', 'category': 'Image', 'website': 'https://canva.com', 'description': 'AI-powered design tool', 'access_type': 'Freemium'},
            
            # Code tools
            {'name': 'GitHub Copilot', 'category': 'Code', 'website': 'https://github.com/features/copilot', 'description': 'AI code assistant', 'access_type': 'Paid'},
            {'name': 'ChatGPT', 'category': 'Code', 'website': 'https://chatgpt.com', 'description': 'AI coding assistant', 'access_type': 'Freemium'},
            {'name': 'Replit', 'category': 'Code', 'website': 'https://replit.com', 'description': 'Online IDE with AI', 'access_type': 'Freemium'},
            {'name': 'Tabnine', 'category': 'Code', 'website': 'https://tabnine.com', 'description': 'AI code completion', 'access_type': 'Free'},
            
            # Research tools
            {'name': 'Perplexity AI', 'category': 'Research', 'website': 'https://perplexity.ai', 'description': 'AI research assistant', 'access_type': 'Freemium'},
            {'name': 'Elicit', 'category': 'Research', 'website': 'https://elicit.org', 'description': 'Research paper analysis', 'access_type': 'Free'},
            {'name': 'Consensus', 'category': 'Research', 'website': 'https://consensus.app', 'description': 'Scientific research AI', 'access_type': 'Freemium'},
            {'name': 'Scholarcy', 'category': 'Research', 'website': 'https://scholarcy.com', 'description': 'Research paper summarizer', 'access_type': 'Paid'},
            
            # Video tools
            {'name': 'Runway ML', 'category': 'Video', 'website': 'https://runwayml.com', 'description': 'AI video editing', 'access_type': 'Paid'},
            {'name': 'Synthesia', 'category': 'Video', 'website': 'https://synthesia.io', 'description': 'AI video generation', 'access_type': 'Paid'},
            {'name': 'Pictory', 'category': 'Video', 'website': 'https://pictory.ai', 'description': 'Video creation from text', 'access_type': 'Freemium'},
            {'name': 'Lumen5', 'category': 'Video', 'website': 'https://lumen5.com', 'description': 'AI video maker', 'access_type': 'Freemium'},
            
            # Audio tools
            {'name': 'Mubert', 'category': 'Audio', 'website': 'https://mubert.com', 'description': 'AI music generation', 'access_type': 'Freemium'},
            {'name': 'Suno AI', 'category': 'Audio', 'website': 'https://suno.ai', 'description': 'AI song creation', 'access_type': 'Free'},
            {'name': 'ElevenLabs', 'category': 'Audio', 'website': 'https://elevenlabs.io', 'description': 'AI voice synthesis', 'access_type': 'Freemium'},
            
            # Writing tools
            {'name': 'Jasper', 'category': 'Writing', 'website': 'https://jasper.ai', 'description': 'AI writing assistant', 'access_type': 'Paid'},
            {'name': 'Copy.ai', 'category': 'Writing', 'website': 'https://copy.ai', 'description': 'AI copywriting tool', 'access_type': 'Freemium'},
            {'name': 'Grammarly', 'category': 'Writing', 'website': 'https://grammarly.com', 'description': 'Writing enhancement', 'access_type': 'Freemium'},
            
            # Productivity tools
            {'name': 'Notion AI', 'category': 'Productivity', 'website': 'https://notion.so', 'description': 'AI-powered workspace', 'access_type': 'Freemium'},
            {'name': 'ClickUp', 'category': 'Productivity', 'website': 'https://clickup.com', 'description': 'AI project management', 'access_type': 'Freemium'},
            
            # Design tools
            {'name': 'Figma AI', 'category': 'Design', 'website': 'https://figma.com', 'description': 'AI design assistant', 'access_type': 'Freemium'},
            {'name': 'Adobe Firefly', 'category': 'Design', 'website': 'https://adobe.com/firefly', 'description': 'Adobe AI design tool', 'access_type': 'Paid'},
        ]
        
        # Create tools
        tools = {}
        for tool_data in tools_data:
            tool, created = Tool.objects.get_or_create(
                name=tool_data['name'],
                defaults={
                    'category': categories[tool_data['category']],
                    'website': tool_data['website'],
                    'description': tool_data['description'],
                    'access_type': tool_data['access_type']
                }
            )
            tools[tool_data['name']] = tool
            if created:
                self.stdout.write(f'Created tool: {tool.name}')
        
        # Create a test user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'test@example.com',
                'first_name': 'Test',
                'last_name': 'User'
            }
        )
        if created:
            user.set_password('testpass123')
            user.save()
            self.stdout.write('Created test user: testuser')
        
        # Create sample reviews
        review_count = 0
        for tool in tools.values():
            # Create 1-3 reviews per tool
            for i in range(random.randint(1, 3)):
                stars = random.randint(3, 5)  # Random rating between 3-5 stars
                review_texts = [
                    f"Great tool for {tool.category.name.lower()} work!",
                    f"Really helpful for my projects.",
                    f"Excellent AI capabilities.",
                    f"Worth the investment.",
                    f"Easy to use and powerful."
                ]
                
                review, created = Review.objects.get_or_create(
                    user=user,
                    tool=tool,
                    defaults={
                        'stars': stars,
                        'review': random.choice(review_texts)
                    }
                )
                if created:
                    review_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {len(categories)} categories, {len(tools)} tools, and {review_count} reviews!'
            )
        )
        self.stdout.write('You can now view the analytics dashboard with pie charts.') 