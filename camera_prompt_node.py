class CameraPromptGenerator:
    """
    相机提示词生成节点
    根据旋转角度、前进距离、垂直角度和镜头类型生成相机运动提示词
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Rotate_Right_to_Left": ("INT", {
                    "default": 0,
                    "min": -90,
                    "max": 90,
                    "step": 1,
                    "display": "slider"
                }),
                "Move_Forward_to_Close_Up": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 10,
                    "step": 1,
                    "display": "slider"
                }),
                "Bird_View_to_Worm_View": ("FLOAT", {
                    "default": 0.0,
                    "min": -1.0,
                    "max": 1.0,
                    "step": 1,
                    "display": "slider"
                }),
                "WideAngle_Lens": ("BOOLEAN", {
                    "default": False,
                    "label_on": "enabled",
                    "label_off": "disabled"
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "camera/prompt"
    
    def generate_prompt(self, Rotate_Right_to_Left, Move_Forward_to_Close_Up, Bird_View_to_Worm_View, WideAngle_Lens):
        """
        生成相机提示词
        """
        prompt_parts = []
        
        # Rotation
        if Rotate_Right_to_Left != 0:
            direction = "left" if Rotate_Right_to_Left > 0 else "right"
            if direction == "left":
                prompt_parts.append(f"将镜头向左旋转{abs(Rotate_Right_to_Left)}度 Rotate the camera {abs(Rotate_Right_to_Left)} degrees to the left.")
            else:
                prompt_parts.append(f"将镜头向右旋转{abs(Rotate_Right_to_Left)}度 Rotate the camera {abs(Rotate_Right_to_Left)} degrees to the right.")
        
        # Move forward / close-up
        if Move_Forward_to_Close_Up > 5:
            prompt_parts.append("将镜头转为特写镜头 Turn the camera to a close-up.")
        elif Move_Forward_to_Close_Up >= 1:
            prompt_parts.append("将镜头向前移动 Move the camera forward.")
        
        # Vertical tilt
        if Bird_View_to_Worm_View <= -1:
            prompt_parts.append("将相机转向鸟瞰视角 Turn the camera to a bird's-eye view.")
        elif Bird_View_to_Worm_View >= 1:
            prompt_parts.append("将相机切换到仰视视角 Turn the camera to a worm's-eye view.")
        
        # Lens option
        if WideAngle_Lens:
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

