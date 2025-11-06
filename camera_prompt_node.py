class CameraPromptGenerator:
    """
    相机提示词生成节点
    根据旋转角度、前进距离、垂直角度和镜头类型生成相机运动提示词
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "rotate_deg": ("INT", {
                    "default": 0,
                    "min": -90,
                    "max": 90,
                    "step": 1,
                    "display": "slider"
                }),
                "move_forward": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 10,
                    "step": 1,
                    "display": "slider"
                }),
                "vertical_tilt": ("FLOAT", {
                    "default": 0.0,
                    "min": -1.0,
                    "max": 1.0,
                    "step": 0.1,
                    "display": "slider"
                }),
                "wideangle": ("BOOLEAN", {
                    "default": False
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "camera/prompt"
    
    def generate_prompt(self, rotate_deg, move_forward, vertical_tilt, wideangle):
        """
        生成相机提示词
        """
        prompt_parts = []
        
        # Rotation
        if rotate_deg != 0:
            direction = "left" if rotate_deg > 0 else "right"
            if direction == "left":
                prompt_parts.append(f"将镜头向左旋转{abs(rotate_deg)}度 Rotate the camera {abs(rotate_deg)} degrees to the left.")
            else:
                prompt_parts.append(f"将镜头向右旋转{abs(rotate_deg)}度 Rotate the camera {abs(rotate_deg)} degrees to the right.")
        
        # Move forward / close-up
        if move_forward > 5:
            prompt_parts.append("将镜头转为特写镜头 Turn the camera to a close-up.")
        elif move_forward >= 1:
            prompt_parts.append("将镜头向前移动 Move the camera forward.")
        
        # Vertical tilt
        if vertical_tilt <= -1:
            prompt_parts.append("将相机转向鸟瞰视角 Turn the camera to a bird's-eye view.")
        elif vertical_tilt >= 1:
            prompt_parts.append("将相机切换到仰视视角 Turn the camera to a worm's-eye view.")
        
        # Lens option
        if wideangle:
            prompt_parts.append(" 将镜头转为广角镜头 Turn the camera to a wide-angle lens.")
        
        final_prompt = " ".join(prompt_parts).strip()
        result = final_prompt if final_prompt else "no camera movement"
        
        return (result,)


# 节点映射
NODE_CLASS_MAPPINGS = {
    "CameraPromptGenerator": CameraPromptGenerator
}

# 节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "CameraPromptGenerator": "Camera Prompt Generator 📷"
}

