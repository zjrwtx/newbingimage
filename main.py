import gradio as gr
from BingImageCreator import ImageGenAsync
import asyncio


import gradio as gr
from BingImageCreator import ImageGenAsync
import asyncio


async def async_image_gen(keyword: str, output_dir: str) -> None:
    async with ImageGenAsync("此处填写你的-U值") as image_generator:
        images = await image_generator.get_images(keyword)
        await image_generator.save_images(images, output_dir=output_dir)


def generate_wallpapers(keyword, output_dir):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_image_gen(keyword, output_dir))


inputs = [
    gr.inputs.Textbox(label="请输入搜索关键字", default="Hong Kong, Seaside, 4K, Anime "),
    gr.inputs.Textbox(label="请输入保存路径", default="./output")
]

outputs = gr.outputs.Textbox(label="状态")


gr.Interface(
    fn=generate_wallpapers,
    inputs=inputs,
    outputs=outputs,
    title="Bing 壁纸生成器",
    description="通过关键词获取 Bing 搜索引擎上与其相关的壁纸图片，并保存到指定文件夹中。",
    theme="light",
    layout="vertical"
).launch()
