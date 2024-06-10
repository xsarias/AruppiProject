from backend.user_profile_subsystem.collection_strategy import FavoritesStrategy, RecommendedStrategy, QueueStrategy
from backend.user_profile_subsystem.collection import Collection

class User:
    """This class manages the user collections"""
    def __init__(self, username):
        self.username = username
        self.favorites = Collection(FavoritesStrategy())
        self.queue = Collection(QueueStrategy())
        self.recommended = Collection(RecommendedStrategy())

    def add_to_favorites(self, anime_id):
        self.favorites.add_to_collection(anime_id)

    def add_to_recommended(self, anime_id):
        self.recommended.add_to_collection(anime_id)

    def add_to_queue(self, anime_id):
        self.queue.add_to_collection(anime_id)

    def show_favorites(self):
        self.favorites.show_collection()

    def show_recommended(self):
        self.recommended.show_collection()

    def show_queue(self):
        self.queue.show_collection()

# Bloque de prueba
if __name__ == "__main__":
    # Crear un usuario
    user = User("Xiomara")

    # Añadir animes a las colecciones
    user.add_to_favorites("Naruto")
    user.add_to_favorites("One Piece")
    user.add_to_recommended("Attack on Titan")
    user.add_to_queue("My Hero Academia")

    # Mostrar las colecciones
    print("Favorites:", end=" ")
    user.show_favorites()       # Output: Favorites: ['Naruto', 'One Piece']
    
    print("Recommended:", end=" ")
    user.show_recommended()     # Output: Recommended: ['Attack on Titan']
    
    print("Queue:", end=" ")
    user.show_queue()           # Output: Queue: ['My Hero Academia']
