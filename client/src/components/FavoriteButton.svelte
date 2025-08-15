<script lang="ts">
  export let dogId: number;
  export let isFavorite: boolean = false;
  export let onToggle: (id: number, next: boolean) => void = () => {};

  async function toggle() {
    const res = await fetch('/api/favorites', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: dogId })
    });
    if (!res.ok) return;
    const data = await res.json();
    onToggle(dogId, !!data.favorite);
  }
</script>

<button aria-label={isFavorite ? 'Unfavorite' : 'Favorite'} on:click={toggle}
  class="inline-flex items-center justify-center h-8 w-8 rounded-full transition transform duration-150 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500"
  class:scale-110={isFavorite}
>
  <span class={isFavorite ? 'text-pink-500' : 'text-gray-400'}>❤</span>
</button>

<style>
  button.scale-110 { filter: drop-shadow(0 0 6px rgba(236, 72, 153, 0.35)); }
  button:hover { transform: scale(1.1); }
</style>
