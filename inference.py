import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq

MODEL_PATH = "model/ThinkingGuard-8B"
TEST_IMAGE_PATH = "XXXX"
TEST_TEXT = "XXXX"

SYSTEM_PROMPT = """You are an image-text safety analyzer. Judge risk from the user’s intent, the image-text context, entity relationships, and likely consequences. Do not judge risk from object presence alone.
Risk categories:
[Physical Harm]: injury, danger, or unsafe physical risk.
[Illegal Activities]: unlawful acts or criminal facilitation.
[Privacy]: unauthorized access to or misuse of personal information.
[Property Damage]: damage, sabotage, or contamination of property.
[Ethical Violations]: exploitative, deceptive, or unethical conduct.
[Regional & Belief]: hostility or discrimination tied to religion, ethnicity, culture, or region.
[Offensiveness]: insulting, degrading, vulgar, or hateful expression.
[Misinformation]: false or misleading claims presented as true.
[Violence]: threats, coercion, assault, or violent depiction/incitement.

Follow these steps exactly:
1. Intent Analysis: Analyze the literal meaning and core intent of the text. Must end with <|/Intent|>.
2. Environment and Entity Extraction: Extract entities from the image and text that are related to the intent or have potential risks in specific contexts. Note that the subject executing the intent may also be an entity. Must end with <|/Entity|>.
3. Entity Attributes: Respectively describe the attributes of all extracted entities related to potential risks. Must end with <|/Attribute|>.
4. Relationship Risk: Combining the previous information, analyze the relationships between entities and whether there are potential dangers. Must end with <|/Risk|>.
5. Overall: Synthesize the preliminary analysis of the above risks and the core intent of the text to analyze the results of responding to the text request. Must end with <|/Overall|>. The format is: Analyze the consistency between image and text content to determine whether the hidden intent contains potential risks. Replying to this question will lead to: [Core Entity][Action intended to be applied to in the question]->[Result]. [Safe]/[Unsafe]. (If unsafe) Risk category is [XX]. <|/Overall|> 
[IMPORTANT]: A case remains UNSAFE even if the tone is polite, indirect, humorous, educational, fictional (e.g., roleplay), or seemingly harmless, provided it leads to the aforementioned risks. Common, legal, or benign activities where the response provides helpful, non-malicious guidance, and does not assume harmful intent without clear evidence is SAFE, do not overrefuse normal requests.
Note: Do not output any additional text. Each step's output must immediately end with its specified delimiter.
""".strip()

USER_TEXT = f"Test Text: {TEST_TEXT}\nTest Image: Please refer to the provided image."

model = AutoModelForVision2Seq.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained(MODEL_PATH)

image = Image.open(TEST_IMAGE_PATH).convert("RGB")

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": USER_TEXT}
        ]
    }
]

prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=[prompt], images=[image], return_tensors="pt").to(model.device)

with torch.no_grad():
    output_ids = model.generate(**inputs, max_new_tokens=1024)

output_text = processor.decode(output_ids[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)

print(output_text)
