import gradio as gr
from BingImageCreator import ImageGenAsync
import asyncio


import gradio as gr
from BingImageCreator import ImageGenAsync
import asyncio


async def async_image_gen(keyword: str, output_dir: str) -> None:
    async with ImageGenAsync("xxxxx") as image_generator:
        images = await image_generator.get_images(keyword)
        await image_generator.save_images(images, output_dir=output_dir)


def generate_wallpapers(keyword, output_dir):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_image_gen(keyword, output_dir))


inputs = [
    gr.inputs.Textbox(label="请输入你想生成的图片是什么样的（语言必须是英文，可以用翻译软件转为英文再复制到这里）", default="Hong Kong, Seaside, 4K, Anime "),
    gr.inputs.Textbox(label="请输入保存路径，建议默认就好", default="./output")
]

outputs = gr.outputs.Textbox(label="状态")


gr.Interface(
    fn=generate_wallpapers,
    inputs=inputs,
    outputs=outputs,
    title="小译AI-新必应图片生成的简易可视化界面",
    description="无需代理和代码基础、小白三步也能拿下AI绘画||公众号：正经人王同学",
    theme="light",
    layout="vertical"
).launch()
