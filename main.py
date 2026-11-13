import time
import random
from vision_engine import VisionSystem

class ActionManager:
    """Simula as ações no jogo"""
    def move_to(self, x, y):
        pass 
    
    def interact(self):
        # Simula interação suave
        return "Interagiu"

    def teleport(self, x, y):
        print(f"TP para {x},{y}")

    def break_chest_manual(self):
        print("Quebrou o baú na mão!")

class HackEngine:
    def __init__(self):
        self.vision = VisionSystem()
        self.actions = ActionManager()
        self.is_running = False
        self.mode = None

    def start(self, mode):
        self.mode = mode
        self.is_running = True
        while self.is_running:
            if mode == 'root':
                self.run_root_mode()
            else:
                self.run_semi_root_mode()

    def run_root_mode(self):
        """Modo Cheat Puro (Root)"""
        chests = [{'x': 100, 'y': 200}, {'x': 400, 'y': 600}]
        for c in chests:
            if not self.is_running: break
            self.actions.teleport(c['x'], c['y'])
            time.sleep(0.5)

    def run_semi_root_mode(self):
        """Modo Sem Root com Lógica 50/50 e ESP"""
        env = self.vision.scan_environment()
        target = self.vision.get_best_target()

        if not target:
            time.sleep(0.5)
            return

        if target['type'] == 'ENEMY':
            # Fugir ou se esconder
            self.vision.current_state = "RUNNING_AWAY"
            self.actions.move_to(random.randint(100, 700), random.randint(100, 600))
            time.sleep(1)
            self.vision.current_state = "IDLE"
            return

        if target['type'] == 'CHEST':
            chest = target['data']
            # Ir até o baú
            self.actions.move_to(chest['pos']['x'], chest['pos']['y'])
            time.sleep(0.5)
            
            # AÇÃO 50/50
            roll = random.random()
            if roll < 0.5:
                # 50% Abre Normal
                self.actions.interact()
                return "Abriu normalmente"
            else:
                # 50% Quebra na Mão
                self.actions.break_chest_manual()
                return "Quebrou na mão"
                
            time.sleep(0.5)

    def stop(self):
        self.is_running = False