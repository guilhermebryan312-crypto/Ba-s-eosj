import random

class VisionSystem:
    """
    Sistema de Visão Avançado para Modo Sem Root.
    - Detecta Inimigos (Aura Vermelha)
    - Identifica Portas e Paredes (Lógica de Casa)
    - Roteamento Inteligente (Correr/Fugir)
    """
    def __init__(self):
        self.players = []
        self.chests = []
        self.doors = []
        self.walls = []
        
        # Estado de Ameaça
        self.nearest_enemy_dist = float('inf')
        self.is_threat_nearby = False
        self.current_state = "IDLE" 

    def scan_environment(self):
        """Varre o ambiente simulando a câmera."""
        self.players = []
        self.chests = []
        self.doors = []
        self.walls = []

        # 1. Detecção de Inimigos (Aura Vermelha)
        if random.random() < 0.3:
            enemy = {
                'id': random.randint(100, 999),
                'is_enemy': True,
                'hp': random.randint(10, 100),
                'distance': random.randint(2, 15), 
                'pos': {'x': random.randint(100, 700), 'y': random.randint(100, 600)}
            }
            self.players.append(enemy)
            if enemy['distance'] < self.nearest_enemy_dist:
                self.nearest_enemy_dist = enemy['distance']
                self.is_threat_nearby = True
        else:
            self.is_threat_nearby = False
            self.nearest_enemy_dist = float('inf')

        # 2. Detecção de Baús (ESP)
        if random.random() < 0.4:
            self.chests.append({
                'id': random.randint(1, 100),
                'is_open': False,
                'distance': random.randint(10, 80),
                'pos': {'x': random.randint(100, 700), 'y': random.randint(100, 600)}
            })

        # 3. Identificação de Estruturas (Portas/Paredes)
        if random.random() < 0.2:
            self.doors.append({
                'id': random.randint(1, 50),
                'pos': {'x': random.randint(100, 700), 'y': random.randint(100, 600)}
            })

        return {
            'players': self.players,
            'chests': self.chests,
            'doors': self.doors,
            'threat_level': self.is_threat_nearby,
            'nearest_enemy': self.players[0] if self.players else None
        }

    def get_best_target(self):
        """Escolhe o melhor alvo baseado no estado atual"""
        if self.is_threat_nearby and self.current_state != "HIDING":
            return {'type': 'ENEMY', 'data': self.players[0]}
        
        if self.chests:
            sorted_chests = sorted(self.chests, key=lambda k: k['distance'])
            return {'type': 'CHEST', 'data': sorted_chests[0]}
            
        if self.doors:
            return {'type': 'DOOR', 'data': self.doors[0]}

        return None