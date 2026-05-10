"""Run once to populate the SQLite database with all portfolio data."""
import json

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)


def seed():
    db = SessionLocal()

    if db.query(models.Profile).count() > 0:
        print("Database already seeded. Delete portfolio.db to re-seed.")
        db.close()
        return

    # ---- PROFILE ----
    db.add(models.Profile(
        name="E. Mohan Kumar",
        title="Video Editor & Graphic Designer",
        tagline="I turn raw footage and bold ideas into cinematic experiences that captivate, convert, and leave a lasting impression.",
        location="Chennai, India",
        email="mohankumar2604@gmail.com",
        phone="+91 88258 61943",
        whatsapp_url="https://wa.me/918825861943",
        instagram_url="https://www.instagram.com/mohankumar_264/",
        youtube_url="https://www.youtube.com/playlist?list=PLotghfO6ldjp5GdMznkT4cB_PircX7fXf",
        linkedin_url="https://linkedin.com/in/mohan-kumar-59ab601b8",
        facebook_url="https://www.facebook.com/profile.php?id=100009469471304",
        profile_image="http://localhost:8000/assets/Profile/profile.jpg",
        years_experience="3+",
        projects_done="50+",
        happy_clients="15+",
        platforms_mastered="3",
        about_text_1="I'm a Chennai-based Video Editor & Graphic Designer with over 3 years of hands-on experience turning ideas into stunning visual content. Currently creating at Penflock & Trillion Thoughts Technologies, I specialize in cinematic storytelling that drives real results.",
        about_text_2="From social media reels to full-scale promotional films, I blend technical precision with creative intuition — always chasing the frame that makes someone stop scrolling.",
    ))

    # ---- PORTFOLIO ITEMS ----
    portfolio_items = [
        # Kinetic & Stomp — local thumbnails served via API
        dict(title="Video 1", category="kineatic-stomp",
             category_label="Kineatic and Stomp Typographic Videos",
             description="Kineatic and Stomp Typographic Video",
             drive_id="1eREZXf67T2ivna5ot1SFl2YhmXE_fRoh",
             thumbnail_url="http://localhost:8000/assets/thumbnails/video1_thumb.png",
             sort_order=1),
        dict(title="Video 3", category="kineatic-stomp",
             category_label="Kineatic and Stomp Typographic Videos",
             description="Kineatic and Stomp Typographic Video",
             drive_id="1HRoCQJFQ7-PPlTorZdyIx0EmDqf4UgUw",
             thumbnail_url="http://localhost:8000/assets/thumbnails/video3_thumb.png",
             sort_order=2),
        # Reels & Shorts — Drive thumbnails
        dict(title="Video 2", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1wkQernxvuugJ-zT0XVRtTta2ZxdaG-UB",
             thumbnail_url="https://drive.google.com/thumbnail?id=1wkQernxvuugJ-zT0XVRtTta2ZxdaG-UB&sz=w800-h600",
             sort_order=3),
        dict(title="Video 3", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1O03Vh6Tz8t4ozANhbrQDwLhN7jxOHNRp",
             thumbnail_url="https://drive.google.com/thumbnail?id=1O03Vh6Tz8t4ozANhbrQDwLhN7jxOHNRp&sz=w800-h600",
             sort_order=4),
        dict(title="Video 4", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1W2IQOgmVsRxXJZ5JeOUOaXLEgRrQTHA9",
             thumbnail_url="https://drive.google.com/thumbnail?id=1W2IQOgmVsRxXJZ5JeOUOaXLEgRrQTHA9&sz=w800-h600",
             sort_order=5),
        dict(title="Video 5", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1pWK9OYZ-xdiXZvKePd-rpOElBLvQlAQS",
             thumbnail_url="https://drive.google.com/thumbnail?id=1pWK9OYZ-xdiXZvKePd-rpOElBLvQlAQS&sz=w800-h600",
             sort_order=6),
        dict(title="Video 6", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1S-QOIpBMS1_25sb2807tcKc4De6bpVQg",
             thumbnail_url="https://drive.google.com/thumbnail?id=1S-QOIpBMS1_25sb2807tcKc4De6bpVQg&sz=w800-h600",
             sort_order=7),
        dict(title="Video 7", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1r59A1KUKbYPkAVAdnKHj_JcCnLoNq4hX",
             thumbnail_url="https://drive.google.com/thumbnail?id=1r59A1KUKbYPkAVAdnKHj_JcCnLoNq4hX&sz=w800-h600",
             sort_order=8),
        dict(title="Video 8", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1KcPXWHCJ8IGMyg3esFNtx2ef30i7zN3y",
             thumbnail_url="https://drive.google.com/thumbnail?id=1KcPXWHCJ8IGMyg3esFNtx2ef30i7zN3y&sz=w800-h600",
             sort_order=9),
        dict(title="Video 9", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1nZKL8V06vdR1fJ_k6_KBKDhNntgDbUn-",
             thumbnail_url="https://drive.google.com/thumbnail?id=1nZKL8V06vdR1fJ_k6_KBKDhNntgDbUn-&sz=w800-h600",
             sort_order=10),
        dict(title="Video 10", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1ujj1vQUdPXlQx5K2OZ-U7Tet2qSWgr26",
             thumbnail_url="https://drive.google.com/thumbnail?id=1ujj1vQUdPXlQx5K2OZ-U7Tet2qSWgr26&sz=w800-h600",
             sort_order=11),
        dict(title="Video 11", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="107DIrd5zTca_yG2Y-PITvtPfKcmIoMCA",
             thumbnail_url="https://drive.google.com/thumbnail?id=107DIrd5zTca_yG2Y-PITvtPfKcmIoMCA&sz=w800-h600",
             sort_order=12),
        dict(title="Video 12", category="reels-shorts",
             category_label="Reels and Shorts Videos",
             description="Reels and Shorts Video",
             drive_id="1ub7g62VSqFavWJFsfqc_8kCP9pAxLTH8",
             thumbnail_url="https://drive.google.com/thumbnail?id=1ub7g62VSqFavWJFsfqc_8kCP9pAxLTH8&sz=w800-h600",
             sort_order=13),
    ]
    for item in portfolio_items:
        db.add(models.PortfolioItem(**item))

    # ---- SERVICES ----
    services = [
        dict(icon="🎬", title="Video Editing",
             description="High-impact edits for YouTube, Instagram, ads, and branded content that tell your story compellingly.",
             items_json=json.dumps(["YouTube Longform & Shorts", "Instagram Reels & Stories", "Promotional & Ad Videos", "Color Grading & Audio Sync"]),
             sort_order=1),
        dict(icon="🖌️", title="Graphic Design",
             description="Bold, memorable visuals from social media creatives and posters to full brand identity systems.",
             items_json=json.dumps(["Poster & Banner Design", "Logo & Brand Identity", "YouTube Thumbnails", "Social Media Templates"]),
             sort_order=2),
        dict(icon="⚡", title="Motion Graphics",
             description="Fluid animations, logo intros, and kinetic typography that elevate any content above the noise.",
             items_json=json.dumps(["Logo Reveal Animations", "Animated Explainers", "Title Sequences"]),
             sort_order=3),
        dict(icon="📣", title="Social Media",
             description="Strategic content creation and management for Instagram and YouTube that grows your brand presence.",
             items_json=json.dumps(["Content Strategy & Planning", "Reels & Short-form Video", "Visual Brand Consistency", "Engagement-focused Creatives"]),
             sort_order=4),
    ]
    for s in services:
        db.add(models.Service(**s))

    # ---- SKILLS ----
    skills = [
        dict(icon_text="Pr", icon_class="pr", name="Adobe Premiere Pro", percentage=92, description="92% · Primary Video Editor", sort_order=1),
        dict(icon_text="Ae", icon_class="ae", name="Adobe After Effects", percentage=85, description="85% · Motion Graphics & VFX", sort_order=2),
        dict(icon_text="Ps", icon_class="ps", name="Adobe Photoshop", percentage=90, description="90% · Photo & Graphic Design", sort_order=3),
        dict(icon_text="Ai", icon_class="ai", name="Adobe Illustrator", percentage=50, description="50% · Vector & Brand Design", sort_order=4),
    ]
    for sk in skills:
        db.add(models.Skill(**sk))

    # ---- TESTIMONIALS ----
    testimonials = [
        dict(client_name="Riazkhan", client_role="Director, ARK Studios",
             text="Mohan delivered exceptional video edits for our brand's Instagram reels. The quality, timing, and creativity were on another level. Our engagement doubled within the first month. Highly recommend!",
             stars=5, sort_order=1),
        dict(client_name="Marketing Head", client_role="Penflock Technologies",
             text="Working with Mohan was seamless. He understood our brand identity immediately and translated it into visuals that resonated with our audience. Professional, punctual, and incredibly talented.",
             stars=5, sort_order=2),
        dict(client_name="Yeshwanth", client_role="YouTube Content Creator",
             text="The logo intro and motion graphics Mohan created for us were absolutely cinematic. Our channel's watch time increased significantly. He's a go-to for any serious content creator.",
             stars=5, sort_order=3),
    ]
    for t in testimonials:
        db.add(models.Testimonial(**t))

    db.commit()
    db.close()
    print("Database seeded successfully!")


if __name__ == "__main__":
    seed()
